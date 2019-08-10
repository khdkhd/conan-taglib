from conans import ConanFile, CMake, tools


class TaglibConan(ConanFile):
    name = "taglib"
    version = "1.11.1"
    license = "LGPL"
    author = "Julien Graziano julien@graziano.fr"
    url = "<Package recipe repository url here, for issues about the package>"
    description = """
        TagLib is a library for reading and editing the metadata of several popular audio formats.
    """
    topics = ("ID3v1", "ID3v2")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/taglib/taglib.git")
        self.run("cd taglib && git checkout v{}".format(self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="taglib", defs={
            "BUILD_SHARED_LIBS": "ON" if self.options.shared else "OFF"
        })
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["tag"]

