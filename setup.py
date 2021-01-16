from setuptools import setup
setup(
    name = "python-amplitude-export", 
    packages = ["amplitude"], 
    version = "0.0.1", 
    license="MIT", 
    description = "Python wrapper for Amplitude Export API", 
    author = "Faisal Malik Widya Prasetya", 
    author_email = "faisalmalikwidyaprasetya@gmail.com", 
    url = "https://github.com/MasiCal354/python-amplitude-export", 
    download_url = "https://github.com/MasiCal354/python-amplitude-export/archive/v_01.tar.gz", 
    keywords = ["amplitude", "export", "api"], 
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha", 
        "Intended Audience :: Developers", 
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python :: 3", 
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)