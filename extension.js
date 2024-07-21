const vscode = require('vscode');
const axios = require('axios');

function activate(context) {
    let disposable = vscode.commands.registerCommand('extension.completeCode', async function () {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active text editor found');
            return;
        }
        const prompt = editor.document.getText(editor.selection);
        if (!prompt) {
            vscode.window.showErrorMessage('No text selected');
            return;
        }
        try {
            const response = await axios.post('http://localhost:5000/complete', { prompt });
            const completion = response.data;
            editor.edit(editBuilder => {
                editBuilder.replace(editor.selection, completion);
            });
        } catch (error) {
            vscode.window.showErrorMessage('Error fetching code completion: ' + error.message);
        }
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
