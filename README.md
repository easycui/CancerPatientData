# Cancer patient data 
The web application displays and manages the data of cancer patients. 

## How to use it
At the right side of webpage:
In Summary tab, the histogram charts of the 6 attributes are shown. 
Patients tab shows a data table of cancer patients. The initialized table shows all the data in database.

At the left side of webpage:
In filter tab, you can fill the conditions for the filter. You don't need to fill all of the conditions. After you fill the conditions, you can click the **submit** botton.
Then the table in Patients wil show the result of filtering.

In New Patient tab, you can add the data for new patients. The system will automatically generate the patient_ID.

## Framework

The backend framework of this project is **Django**.
The database is **MySQL**.
The frontend framework is **Bootstrap** and  **JQuery**

3rd party js plugins:

* CanvasJS
* Datatables

## Deployment

If you want to deploy this project on your host(Linux), you may need to install following package:

* python 2.7
* numpy (Python package)
* Django
* MySQL-client
* libmysqlclient-dev
* Mysqldb (python package)

If all of these packages(software) have been installed, run 

```python
python manage.py runserver 8000
```

in folder **patient/mysite/**

Then open web address [127.0.0.1:8000/patients](127.0.0.1:8000/patients).


## Versioning

1.0

## Authors

* **Yuxin Cui** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

