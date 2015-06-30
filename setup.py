from distutils import core
from distutils.core import Command
import sys

class TestCommand(Command):

    description = "Run self-test"

    # Long option name, short option name, description
    user_options = [
        ('skip-slow-tests', None,
         'Skip slow tests'),
        ('module=', 'm', 'Test a single module (e.g. Cipher, PublicKey)')
    ]

    def initialize_options(self):
        self.build_dir = None
        self.skip_slow_tests = None
        self.module = None

    def finalize_options(self):
        self.set_undefined_options('install', ('build_lib', 'build_dir'))
        self.config = {'slow_tests': not self.skip_slow_tests}

    def run(self):
        # Run sub commands
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        # Run SelfTest
        self.announce("running self-tests")
        old_path = sys.path[:]
        try:
            sys.path.insert(0, self.build_dir)
            from Crypto import SelfTest
            moduleObj = None
            if self.module:
                if self.module.count('.')==0:
                    # Test a whole a sub-package
                    full_module = "Crypto.SelfTest." + self.module
                    module_name = self.module
                else:
                    # Test only a module
                    # Assume only one dot is present
                    comps = self.module.split('.')
                    module_name = "test_" + comps[1]
                    full_module = "Crypto.SelfTest." + comps[0] + "." + module_name
                # Import sub-package or module
                moduleObj = __import__( full_module, globals(), locals(), module_name )
            SelfTest.run(module=moduleObj, verbosity=self.verbose, stream=sys.stdout, config=self.config)
        finally:
            # Restore sys.path
            sys.path[:] = old_path

        # Run slower self-tests
        self.announce("running extended self-tests")

    sub_commands = [ ('build', None) ]

kw = {'name':"jycrypto",
      'version':"2.7a1",  # See also: lib/Crypto/__init__.py
      'description':"Cryptographic modules for Jython, based off of pycrypto",
      'author':"Casey Marshall",
      'author_email':"casey.s.marshall@gmail.com",
      'url':"https://github.com/csm/jycrypto",

      'cmdclass' : {'test': TestCommand },
      'packages' : ["Crypto", "Crypto.Hash", "Crypto.Cipher", "Crypto.Util",
                    "Crypto.Random",
                    "Crypto.Random.Fortuna",
                    "Crypto.Random.OSRNG",
                    "Crypto.SelfTest",
                    "Crypto.SelfTest.Cipher",
                    "Crypto.SelfTest.Hash",
                    "Crypto.SelfTest.Protocol",
                    "Crypto.SelfTest.PublicKey",
                    "Crypto.SelfTest.Random",
                    "Crypto.SelfTest.Random.Fortuna",
                    "Crypto.SelfTest.Random.OSRNG",
                    "Crypto.SelfTest.Util",
                    "Crypto.SelfTest.Signature",
                    "Crypto.SelfTest.IO",
                    "Crypto.Protocol",
                    "Crypto.PublicKey",
                    "Crypto.Signature",
                    "Crypto.IO"],
      'package_dir' : { "Crypto": "lib/Crypto" }
}

core.setup(**kw)
