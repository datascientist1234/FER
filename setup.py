from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['wheel', 'bar', 'greek','streamlit','numpy','opencv_python','av','tensorflow','aiortc','Pillow','streamlit_webrtc'], #external packages as dependencies
     )
