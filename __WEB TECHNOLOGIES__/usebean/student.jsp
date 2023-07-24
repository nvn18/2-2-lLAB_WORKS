<%-- 
    Document   : index
    Created on : Jul 24, 2023, 10:41:51 AM
    Author     : y21cs185
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Java Use Bean</h1>
        <jsp:useBean id="StudentBean" class="p1.student"/>
        <jsp:setProperty name="StudentBean" property="name" value="neeraj" />
        Get name:
        <jsp:getProperty name="StudentBean" property="name" /> <br/>
        <jsp:setProperty name="StudentBean" property="email" value="nvn18@gamil.com" />
        Get email:
        <jsp:getProperty name="StudentBean" property="email" /> <br/>
        <jsp:setProperty name="StudentBean" property="rollno" value="185" />
        Get roll no.:
        <jsp:getProperty name="StudentBean" property="rollno" /> <br/>

    </body>
</html>
