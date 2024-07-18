package net.ocatide.ui;

import javax.swing.*;

import java.util.ArrayList;
import java.util.List;

import java.awt.event.ActionListener;

public class MenuManager {
    private List<JMenu> menus = new ArrayList<>();

    public MenuManager() {}
    
    public void registerMenu(String menuName) {
        JMenu menu = new JMenu(menuName);
        menus.add(menu);
    }

    public void registerMenuItem(String menuName, String menuItemName, ActionListener al) {
        JMenu menu = new JMenu(menuName);
        JMenuItem menuItem = new JMenuItem(menuItemName);
        menuItem.addActionListener(al);
        menu.add(menuItem);
        if (!menus.contains(menu)) {
            menus.add(menu);
        }
    }

    public void registerSubMenu(String menuName, String subMenuName){
        JMenu menu = new JMenu(menuName);
        if (!menus.contains(menu)) {
            registerMenu(menuName);
        }
        JMenu subMenu = new JMenu(subMenuName);
        menu.add(subMenu);
    }

    public List<JMenu> getMenus() {
        return menus;
    }
}
