package net.ocatide;

import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

import javax.swing.Timer;
import javax.swing.border.BevelBorder;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenuBar;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;

import net.ocatide.interaction.UserInteraction;
import net.ocatide.sticks.StickKind;
import net.ocatide.sticks.Walks;
import net.ocatide.ui.MenuManager;
import net.ocatide.ui.ThemeManager;
import net.ocatide.ui.ThemeManager.Theme;

/**
 * The {@code App} class is the main Orange Cat API´
 * 
 */

@SuppressWarnings ("unused")
public class App {
    public UserInteraction userInteraction = new UserInteraction();
    public ThemeManager themeManager = new ThemeManager();
    public MenuManager menuManager = new MenuManager();

    public String   modName,
                    modVersion,
                    modAuthor,
                    uiThemeName="dark",
                    modDir = "ocatapp";

    public StickKind stick = StickKind.INITIAL;
    public Walks walksd = new Walks();

    public JTextPane code = new JTextPane();
    public JScrollPane scrollCode;
    public App(){}

    public JFrame selfFrame = new JFrame();
    public JMenuBar menuBar = new JMenuBar();

    public void show(){
        giveProperties();
        selfFrame.setLayout(null);
        selfFrame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        selfFrame.setTitle(modName + " ("+modVersion+" By: "+modAuthor+")");
        selfFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        selfFrame.setIconImage(new ImageIcon("assets/"+modDir+"/images/logo.png").getImage());
        new Timer(1, event -> check()).start();
        applyMenus();

        showSticks();

        /**
        SyntaxesManager syntaxesManager = new SyntaxesManager("assets/ocatapp/config/syntaxes/highlight.properties");
        syntaxesManager.applySyntaxHighlighting(txtPane);
        *!*/
        selfFrame.setVisible(true);
    }

    public void showSticks(){
        if(stick == StickKind.CODESPACE){
            code = new JTextPane();
            code.setBounds(10, 50, 1260, 675);
            code.setBackground(themeManager.getTheme(uiThemeName).codearea_bg);
            code.setBorder(new BevelBorder(BevelBorder.RAISED, Color.BLACK, Color.BLACK));
            code.setForeground(themeManager.getTheme(uiThemeName).codearea_fg);
            code.setFont(themeManager.getTheme(uiThemeName).codeareaFont);
            scrollCode = new JScrollPane(code);
            scrollCode.setBounds(10, 10, 1260, 675);
            scrollCode.setBorder(new BevelBorder(BevelBorder.RAISED, Color.BLACK, Color.BLACK));
            selfFrame.add(scrollCode);
        }else if(stick == StickKind.INITIAL) {
            JLabel walks = new JLabel("Walks");
            walks.setForeground(themeManager.getTheme(uiThemeName).foreground_color);
            walks.setBounds(10, 50, 100, 20);
            selfFrame.add(walks);
            int y = 0;
            int Y_STEP =60;
            for (Walks.Walk walk : walksd.walks){
                int y_offset = y* Y_STEP;
                JLabel name = new JLabel(walk.walkName);
                name.setBounds(10, y_offset, 100, 10);
                selfFrame.add(name);
                JLabel description = new JLabel(walk.walkDescription);
                description.setBounds(10, y_offset + 10, 100, 10);
                selfFrame.add(description);
                y ++;
            }
        }
    }

    public void check(){

        applyTheme(uiThemeName);
    }

    public void applyMenus(){
        menuManager.getMenus().forEach(menu -> {
            menuBar.add(menu);
        });
        selfFrame.setJMenuBar(menuBar);
    }

    public void applyTheme(String themeName){
        Container contentPane = selfFrame.getContentPane();

        Theme theme = themeManager.getTheme(themeName);
        contentPane.setBackground(theme.background_color);
    }

    public void giveProperties(){
        String completeDir = "assets/"+modDir+"/config/app.properties";

        Properties properties = new Properties();
        try (FileInputStream fis = new FileInputStream(completeDir)){
            properties.load(fis);
        }catch(IOException e){
            userInteraction.alert(UserInteraction.AlertType.ERROR, "Cannot found app.properties");
        }

        modName = properties.getProperty("app.name");
        modVersion = properties.getProperty("app.version");
        modAuthor = properties.getProperty("app.author");

        uiThemeName = properties.getProperty("ui.theme.default");
    }
}
