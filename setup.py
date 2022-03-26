from setuptools import setup

setup(
    name='PyMoe',
    version='2.0.0',
    packages=['pymoe'],
    url='https://github.com/ccubed/PyMoe',
    license='MIT',
    author='Cooper Click',
    author_email='ccubed.techno@gmail.com',
    description="PyMoe is the only python lib you'll ever need if you need anime/manga on the python platform.",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries'
    ],
    keywords="Anime Manga LN VN VNDB Anilist Kitsu AniDB MyAnimeList MAL Bakatsuki",
    install_requires=['requests', 'bs4', 'ujson']
)
