from distutils.core import setup

setup(name='powerline-mem-segment',
      version='1.0',
      description='Memory segment for Powerline',
      author='Mads Kalør',
      author_email='mads@kaloer.com',
      packages=['powerlinemem'],
      url='https://github.com/mKaloer/powerline_mem_segment',
      download_url='https://github.com/mKaloer/powerline_mem_segment/tarball/1.0',
      install_requires=[
          "psutil"
      ]
     )
