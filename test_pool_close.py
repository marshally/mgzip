import mgzip

for x in range(0, 300):
    fn = "test.gz"
    with mgzip.open(fn, mode='wb') as f:
        f.write(b"testing")

    with mgzip.open(fn, mode='rb') as f:
        print(f.read(), x)
