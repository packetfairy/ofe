import os
import gzip
import time
import base64


class emailobfuscator:
    def decode(self, encoded):
        '''return base64 decoded data'''
        return(base64.b64decode(encoded))

    def encode(self, tmpfile):
        '''return base64 encoded data'''
        r = open(tmpfile, mode='rb')
        data = base64.b64encode(r.read())
        r.close()
        # and, again, we're civilized people.
        os.remove(tmpfile)
        return(data)

    def get_tmp_file(self):
        '''returns a safe tmpfile name'''
        now = str(time.time())
        tmpfile = '/tmp/email_rev_b64_gz.' + now
        return(tmpfile)

    def mygunzip(self, zipped):
        '''return gunzipped data'''
        tmpfile = self.get_tmp_file()
        # open a tmp file to write to, because the gzip module (at least the
        # one I expect is most likely to be there on your system) only operates
        # over files!
        try:
            w = open(tmpfile, 'w')
        except IOError, e:
            print('problem writing file: %' % tmpfile)
            print('check your permissions and try again')
            print e
            exit(0)
        # write your data out to that file
        w.write(zipped)
        w.close()
        # now read it out with gzip
        f = gzip.open(tmpfile, 'rb')
        e = f.read()
        f.close()
        # let's also clean up after ourselves, shall we?
        os.remove(tmpfile)
        return(e)

    def gzip(self, data):
        '''returns filename of gzipped data'''
        # again, open a tmp file to write to, because the gzip module
        # only operates over files!
        tmpfile = self.get_tmp_file()
        # write your data, whatever it is, to it
        o = gzip.open(tmpfile, 'wb')
        o.write(data)
        o.close
        return(tmpfile)

    def reverse(self, reversed_string):
        '''returns reversed string using string[::-1]'''
        return(reversed_string[::-1])

    def ensecretify(self, data):
        '''returns reversed, base64 encoded, and gzipped data'''
        z = self.gzip(data)
        b = self.encode(z)
        r = self.reverse(b)
        return(r)

    def desecretify(self, encoded_string):
        '''returns unreversed, base64 decoded, and gunzipped data'''
        r = self.reverse(encoded_string)
        d = self.decode(r)
        u = self.mygunzip(d)
        return(u)
