**Beginner/Encoding or encryption?**

> Is encoding and encryption the same thing?
> 
> 55 6b 4e 48 65 32 6f 7a 58 32 4e 6f 5a 31 39 6d 4d 48 6f 7a 58 7a 4e 68 63 44 42 78 64 6d 46 30 58 7a 46 68 58 32 77 77 61 47 56 66 4d 32 46 77 5a 57 78 6e 64 6a > 42 68 66 51 3d 3d


This looks like hexadecimals, so we can try to convert them into ascii-text.

´´´bash
hex_str = "55 6b 4e 48 65 32 6f 7a 58 32 4e 6f 5a 31 39 6d 4d 48 6f 7a 58 7a 4e 68 63 44 42 78 64 6d 46 30 58 7a 46 68 58 32 77 77 61 47 56 66 4d 32 46 77 5a 57 78            6e 64 6a 42 68 66 51 3d 3d"
echo $hex_str | xxd -r -p
´´´

Gives the output:
´´´
UkNHe2ozX2NoZ19mMHozXzNhcDBxdmF0XzFhX2wwaGVfM2FwZWxndjBhfQ==
´´´

Which looks like base64 encoding, so we try to decrypt it.
```
echo "UkNHe2ozX2NoZ19mMHozXzNhcDBxdmF0XzFhX2wwaGVfM2FwZWxndjBhfQ==" | base64 -d
> RCG{j3_chg_f0z3_3ap0qvat_1a_l0he_3apelgv0a}
```

