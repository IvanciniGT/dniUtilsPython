from setuptools import setup, find_packages

setup(
    name="dni",
    version="0.3",
    packages=find_packages(exclude=['test']),
    install_requires=[
        # Lista de dependencias si es necesario
    ],
    entry_points={
        'console_scripts': [
            # Puntos de entrada para comandos en la terminal, si es necesario
        ],
    },
    author="Tu Nombre",
    author_email="https://github.com/IvanciniGT/dniUtilsPython.git",
    description="Descripción de tu proyecto",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://tu.url.del.proyecto",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
