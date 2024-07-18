package net.ocatide.interaction;

import javax.swing.*;

@SuppressWarnings ("unused")
public class UserInteraction {
    public UserInteraction(){}

    public enum AlertType {
        ERROR,
        WARNING,
        HINT
    }

    public void alert(AlertType at, String text){
        switch(at){
            case ERROR:
                JOptionPane.showMessageDialog(null, text, "Orange Cat", 
                    JOptionPane.ERROR_MESSAGE);
                break;
            
            case WARNING:
                JOptionPane.showMessageDialog(null, text, "Orange Cat", 
                    JOptionPane.WARNING_MESSAGE);
                break;
            
            case HINT:
                JOptionPane.showMessageDialog(null, text, "Orange Cat", 
                    JOptionPane.QUESTION_MESSAGE);
                break;
        }
    }
}
