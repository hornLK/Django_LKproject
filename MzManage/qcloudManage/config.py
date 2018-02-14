class BaseConfig(object):
    SecretId = "AKIDvmRyNi555zlR0Rd3EIArNhqncLtFaRGt"
    SecretKey = "hInCVfmnjYH1mU9kHi4JWfjho6a6X4a2"

class DevelopmentConfig(BaseConfig):
    pass
class TestConfig(BaseConfig):
   pass
config = {
    "development":DevelopmentConfig,
    "test":TestConfig,
    "default":DevelopmentConfig
}
