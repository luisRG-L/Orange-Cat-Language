import * as vscode from 'vscode';
import { OrangeCatLinter } from './linter/linter';

let diagnosticCollection: vscode.DiagnosticCollection;

export function activate(context: vscode.ExtensionContext) {
    console.log('Orange Cat: Loading...');

    diagnosticCollection = vscode.languages.createDiagnosticCollection('orange-cat-linter');
    context.subscriptions.push(diagnosticCollection);

    vscode.workspace.onDidOpenTextDocument(lintDocument);
    vscode.workspace.onDidSaveTextDocument(lintDocument);

    if(vscode.window.activeTextEditor) {
        lintDocument(vscode.window.activeTextEditor.document);
    }

    console.log('Orange Cat: ready')
}

function lintDocument(document: vscode.TextDocument) {
    if (document.languageId == 'orangecat') {
        let diagnostics = OrangeCatLinter.lintDocument(document);
        diagnosticCollection.set(document.uri, diagnostics);
    }
}

export function desactivate() {
    diagnosticCollection.clear();
}