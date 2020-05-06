from distutils.core import setup

setup(name='powerline-mem-segment',
      version='2.3',
      description='Memory segment for Powerline',
      author='Mads Kaloer',
      author_email='mads@kaloer.com',
      packages=['powerlinemem'],
      url='https://github.com/mKaloer/powerline_mem_segment',
      download_url='https://github.com/mKaloer/powerline_mem_segment/tarball/2.1',
      install_requires=[
          "psutil"
      ]
     )
