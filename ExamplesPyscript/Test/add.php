from pyscript import document

doc = document.HTML()
doc.add(document.button('Add Addresses', id='submit-btn', type='button', py_click='add_address'))

doc.write_to_file('add.php')
