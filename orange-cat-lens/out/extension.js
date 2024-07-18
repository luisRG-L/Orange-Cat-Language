"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.desactivate = exports.activate = void 0;
const vscode = __importStar(require("vscode"));
const linter_1 = require("./linter/linter");
let diagnosticCollection;
function activate(context) {
    console.log('Orange Cat: Loading...');
    diagnosticCollection = vscode.languages.createDiagnosticCollection('orange-cat-linter');
    context.subscriptions.push(diagnosticCollection);
    vscode.workspace.onDidOpenTextDocument(lintDocument);
    vscode.workspace.onDidSaveTextDocument(lintDocument);
    if (vscode.window.activeTextEditor) {
        lintDocument(vscode.window.activeTextEditor.document);
    }
    console.log('Orange Cat: ready');
}
exports.activate = activate;
function lintDocument(document) {
    if (document.languageId == 'orangecat') {
        let diagnostics = linter_1.OrangeCatLinter.lintDocument(document);
        diagnosticCollection.set(document.uri, diagnostics);
    }
}
function desactivate() {
    diagnosticCollection.clear();
}
exports.desactivate = desactivate;
//# sourceMappingURL=extension.js.map