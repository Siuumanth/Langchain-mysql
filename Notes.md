## Steps:


1. Get SQL dump file , 
```bash

mysql -u root -p
#enter password

# create and use a database, then

SOURCE <path to .sql file>

# Then, ur DB is created 

```


## Coding the Chain:

Creating the env:

```bash

python -m venv .venv

.venv/Scripts/activate # to run

deactivate # to deactivate
```

then, get notebook kernel to run notebooks,
`pip install notebook ipykernel`
- and use the selected python in env to execute this