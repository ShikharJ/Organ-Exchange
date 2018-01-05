# Organ-Exchange
A Django-based Web Application Implementing Modified Gale Shapley Algorithm in the Medical Context of Patient - Donor Exchanges.

The idea here is that the institution has the list of available donors and their associated data available at all times,
and patient accounts are accessed to request the transplants keeping in mind the various constraints of medical procedures. 

## Installation
You just need `Python 3.6` or above to run this flawlessly.
 
For a one stop solution, I always use `conda`. First install `conda` and create you own environment as:
```
conda create --name myenv
```
where `myenv` is the environment name (which can be changed at will). Then activate the environment by:
```
source activate myenv
```
and then install `Python` using a single command:
```
conda install -c conda-forge python
```

## Running
You can execute the project using the following command in the `src` folder:
```
python manage.py runserver
``` 

## Screenshots 

![](/screenshots/0.png)

![](/screenshots/1.png)

![](/screenshots/2.png)

![](/screenshots/3.png)

![](/screenshots/4.png)

![](/screenshots/5.png)

![](/screenshots/6.png)

![](/screenshots/7.png)

## Notes and Credits
Since I had no prior experience in web-based designing, I had to rely on a few open source implementations for making the project aesthetically pleasing. Thanks to everyone whose designs helped me in reaching over to a final product. A special shout-out to [Srajan Garg](github.com/srajangarg) and his team's work using CSS and Materialize that helped me in the beautification of the idea implemented above. The core design also helped me in coming up with a rather novel way of representing the data and the algorithm involved.
