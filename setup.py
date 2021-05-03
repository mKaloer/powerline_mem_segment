from distutils.core import setup

setup(name='powerline-mem-segment',
      version='2.4.1',
      description='Memory segment for Powerline',
      author='Mads Kaloer',
      author_email='mads@kaloer.com',
      packages=['powerlinemem'],
      url='https://github.com/mKaloer/powerline_mem_segment',
      install_requires=[
          "psutil"
      ]
     )
