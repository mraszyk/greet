import sys

n = b'icp:public repro'

def enc32(x):
  assert x != 0
  r = b''
  while x != 0:
    b = x % 128
    x //= 128
    if x != 0:
      b += 128
    r += b.to_bytes(1, 'little')
  return r

f = open(sys.argv[1], "rb")
x = f.read()
f.close()

c = str.encode(sys.argv[2])

f = open(sys.argv[1], "wb")
f.write(x)
f.write(b'\x00')
f.write(enc32(len(enc32(len(n))) + len(n) + len(c)))
f.write(enc32(len(n)))
f.write(n)
f.write(c)
f.close()
