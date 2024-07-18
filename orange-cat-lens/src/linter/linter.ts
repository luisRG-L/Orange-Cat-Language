import * as vscode from 'vscode'

export class OrangeCatLinter {
    public static lintDocument(document: vscode.TextDocument): vscode.Diagnostic[] {
        let diagnostics: vscode.Diagnostic[] = [];

        for (let i = 0; i < document.lineCount; i ++){
            let line = document.lineAt(i);
            let text = line.text.trim()
            if(text.includes('TODO') || text.includes('@todo')) {
                let match = /(TODO|@todo)\s+(.+)/i.exec(text);
                if(match){
                    let message = match[0];
                    let diagnostic = new vscode.Diagnostic(
                        line.range,
                        message,
                        vscode.DiagnosticSeverity.Hint
                    );
                    diagnostics.push(diagnostic);
                }
            }
        }

        return diagnostics;
    }
}