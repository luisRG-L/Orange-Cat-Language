package net.ocatide;

import net.ocatide.sticks.Walks.Walk;
import net.ocatide.text.Codes;

public class Mod {
    public Mod(){
        App app = new App();
        start(app);

    }

    public static void main(String[] args) {
        Mod mod = new Mod();
        mod.getClass();
    }

    public void start(App app){
        app.themeManager.modName = "ocatapp";
        app.themeManager.registerTheme("light");
        app.themeManager.registerTheme("dark");
        app.uiThemeName="dark";
        app.menuManager.registerMenu("File");
        app.menuManager.registerMenuItem("Edit", "Font size add", null);
        app.menuManager.registerMenuItem("Snippets", "main method", e -> {
            app.code.setText(app.code.getText() + Codes.Basics.MAIN_METHOD);
        });
        Walk walk = new Walk();
        walk.walkName = "Get Started";
        app.walksd.registerWalk(walk);
        app.show();
    }
}