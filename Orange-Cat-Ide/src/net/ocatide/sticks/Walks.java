package net.ocatide.sticks;

import java.util.List;
import java.util.ArrayList;


public class Walks {
    public Walks(){}

    public static class Walk {
        public String walkName;
        public String walkDescription;
        public String imageCheckRoute = "assets/ocatapp/images/checked.png";
        public String imageUncheckRoute = "assets/ocatapp/images/unchecked.png";
        public boolean isChecked = false;
    }

    public List<Walk> walks = new ArrayList<>();

    public void registerWalk(Walk walk){
        walks.add(walk);
    }
}