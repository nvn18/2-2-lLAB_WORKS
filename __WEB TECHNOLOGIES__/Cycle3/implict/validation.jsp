<%-- 
Document   : Valid2
Created on : 08-Jul-2023, 11:51:15 am
Author     : rosha
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Implicit Objects</title>
</head>
<body>
    <% 
        String uname = request.getParameter("username");
        String pwd = request.getParameter("passwd");
        
        if (uname.equalsIgnoreCase("NVN") && 
            pwd.equalsIgnoreCase("AURORA"))
        {
            out.println("<h1>Login success</h1>");
            out.println("<img src=\"rvrjc.jpg\" width=100 height=100>");
        }
        else
        {
            out.println("<h1 style\"color:red\">Login failed</h1>");
            out.println("<img src=\"webdev.jpg\" width=100 height=100>");

        }
    %>
</body>
</html>