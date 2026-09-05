
<div align="center">

# Password Strength Checker

#### **-by Anirudh J**

### Password Strength Checker using Python
  
A simple and interactive implementation of the Python-based Password Strength Checker that evaluates passwords based on defined security rules such as length, uppercase and lowercase characters, numbers, and special characters, and classifies them as Weak, Moderate, or Strong

<br>

</div> 

## Overview :  
The **Password Strength Checker** is a Python program that evaluates the strength of a password based on multiple security criteria.

The program checks the password length and the presence of uppercase letters, lowercase letters, numbers, and special characters. Based on the number of satisfied conditions, it calculates a strength score and classifies the password as **Weak**, **Moderate**, or **Strong**.

The program also provides a brief rationale when one or more security requirements are not satisfied.

## Security Criteria and Strength Score :
The password is evaluated based on : <br>
Length : <br>
If length is less than 8 : score-> 0 <br>
If length is greater than 8 and less than 12 : score = score + 1<br>
If length is greater than 12 and less than 16 : score = score + 1<br>
If length greater than 16 : score = score + 1<br><br>
Characters : <br>
If uppercase characters present : score = score + 1<br>
If lowercase characters present : score = score + 1<br>
If numbers present : score = score + 1<br>
If special characters present : score = score + 1<br>
<br>
Strength Score : <br>
If score between 1-2 -> Weak password<br>
If score between 3-5 -> Moderated password<br>
If score between 6-7 -> Strong password<br><br>

## Input/Output examples : <br><br>
#### Description : Password is given as input and its score along with reasons are given back as output. <br><br>
I)Input : <br> Enter password: Arithmatrix2006 <br>
  Output : <br> Score: 5 / 6 <br>
Strength: Moderate <br>

Reasons: <br>
No special character<br>

II)Input : <br> Enter password: abcdef <br>
Output : <br> Score: 1 / 6 <br>
Strength: Weak <br>

Reasons: <br>
Password is shorter than 8 characters <br>
No uppercase letter<br>
No number<br>
No special character<br>
