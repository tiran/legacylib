import ctypes as _ctypes

__all__ = ("crypt",)


class _crypt_data(_ctypes.Structure):
    __slots__ = ()
    _fields_ = [
        ("keysched", _ctypes.c_char * 16 * 8),
        ("sb0", _ctypes.c_char * 32768),
        ("sb1", _ctypes.c_char * 32768),
        ("sb2", _ctypes.c_char * 32768),
        ("sb3", _ctypes.c_char * 32768),
        ("crypt_3_buf", _ctypes.c_char * 14),
        ("current_salt", _ctypes.c_char * 2),
        ("current_saltbits", _ctypes.c_int64),
        ("direction", _ctypes.c_int32),
        ("initialized", _ctypes.c_int32),
    ]


try:
    _LIBCRYPT = _ctypes.CDLL("libxcrypt.so")
except OSError:
    try:
        _LIBCRYPT = _ctypes.CDLL("libcrypt.so")
    except OSError:
        raise ImportError("libcrypt / libxcrypt missing")


class _c_text_p(_ctypes.c_char_p):
    @classmethod
    def from_param(cls, value):
        if value is None:
            return None
        if isinstance(value, str):
            return value.encode("utf-8")
        elif isinstance(value, bytes):
            return value
        else:
            raise TypeError(value)


if hasattr(_LIBCRYPT, "crypt_r"):
    _crypt_r = _LIBCRYPT.crypt_r
    _crypt_r.argtypes = (_c_text_p, _c_text_p, _ctypes.POINTER(_crypt_data))
    _crypt_r.restype = _ctypes.c_char_p

    def crypt(key, salt):
        data = _crypt_data()
        return _crypt_r(key, salt, data)


else:
    _crypt = _LIBCRYPT.crypt
    _crypt.argtypes = (c_text_p, c_text_p)
    _crypt.restype = _ctypes.c_char_p

    def crypt(key, salt):
        return _crypt(key, salt)
