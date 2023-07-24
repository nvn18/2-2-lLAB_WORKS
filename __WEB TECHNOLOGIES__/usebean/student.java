/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package p1;

/**
 *
 * @author y21cs185
 */
public class student {

    int rollno;
    String name,email;
    public void setName(String name)
    {
        this.name=name;
    }
    public void setEmail(String email)
    {
        this.email = email;
    }
    public void setRollno(int rollno)
    {
        this.rollno = rollno;
    }

    public String getName()
    {
        return this.name;
    }
    public String getEmail()
    {
        return this.email;
    }
    public int getRollno()
    {
        return this.rollno;
    }
}
