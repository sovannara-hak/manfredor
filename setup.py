from PythonTools import *

package_name = 'manfredor'

setup(name='manfredor',
	  version='0.1',
	  description='Automatic classification of object based on tags.',
	  author='Sovanski',
	  author_email='hak.sovannara@gmail.com',
	  package_dir={package_name:'src'},
	  packages=[package_name],
	  package_data={package_name: []},
	  cmdclass=cmdclass,

	  script_name=script_name,
	  script_args= script_args
	 )
