sll.theme Installation
----------------------

To install sll.theme into the global Python environment (or a workingenv),
using a traditional Zope 2 instance, you can do this:

* When you're reading this you have probably already run 
  ``easy_install sll.theme``. Find out how to install setuptools
  (and EasyInstall) here:
  http://peak.telecommunity.com/DevCenter/EasyInstall

* Create a file called ``sll.theme-configure.zcml`` in the
  ``/path/to/instance/etc/package-includes`` directory.  The file
  should only contain this::

    <include package="sll.theme" />


Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``sll.theme`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        sll.theme
       
* Tell the plone.recipe.zope2instance recipe to install a ZCML slug:

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    zcml =
        sll.theme
      
* Re-run buildout, e.g. with:

    $ ./bin/buildout
        
You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.
