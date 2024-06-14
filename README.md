# dni

Este módulo se encarga de validar un DNI.

## Ejemplo de uso

```python
from dni import DNI

dni = DNI("12345678T")
print(dni.valido) # True
print(dni.numero) # 12345678
print(dni.letra) # T
print(dni.confianza) # 1
```

## Empaquetar con

```bash
pip install setuptools wheel
python setup.py sdist bdist_wheel
```