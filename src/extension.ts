import * as vscode from 'vscode';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export function activate(context: vscode.ExtensionContext) {
    let commands = [
        { command: 'easygpt.autocomplete', endpoint: '/autocomplete', title: 'Code Autocompletion' },
        { command: 'easygpt.refactorCode', endpoint: '/refactor', title: 'Refactor Code' },
        { command: 'easygpt.errorDetection', endpoint: '/error-detection', title: 'Detect & Fix Errors' },
        { command: 'easygpt.summarizeCode', endpoint: '/summarize', title: 'Summarize Code' }
    ];

    commands.forEach(({ command, endpoint, title }) => {
        let disposable = vscode.commands.registerCommand(command, async () => {
            const editor = vscode.window.activeTextEditor;
            if (!editor) {
                vscode.window.showErrorMessage('No active editor found.');
                return;
            }

            const code = editor.document.getText(editor.selection);
            if (!code) {
                vscode.window.showErrorMessage('No code selected.');
                return;
            }

            try {
                const response = await axios.post(`${API_URL}${endpoint}`, { code });
                vscode.window.showInformationMessage(`${title}: ${response.data.suggestions || response.data.refactored || response.data.fixed_code || response.data.summary}`);
            } catch (error) {
                vscode.window.showErrorMessage(`Error: ${error}`);
            }
        });

        context.subscriptions.push(disposable);
    });
}

export function deactivate() {}
