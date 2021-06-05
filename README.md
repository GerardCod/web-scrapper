# Atributos de los objetos tag

He aqui un listado de los atributos a los que podemos acceder de los objetos Tag

| Atributo | Descripción |
| -------- | ----------- |
| parent | Elemento padre|
| parents| Todos los elementos ancestros |
| next_sibling | Siguiente elemento hermano |
| next_siblings | Todos los elementos hermanos luego del elemento actual
| previous_sibling | El anterior elemento hermano a nuestro elemento actual. |
| previous_siblings | Listado de elementos hermanos anteriores a nuestro elemento actual. |
| contents | Listado de todos los elementos hijos |
| children | Iterable de todos los elementos hijos |
| descendants | Generador de todos los elementos hijos de forma recursiva. |