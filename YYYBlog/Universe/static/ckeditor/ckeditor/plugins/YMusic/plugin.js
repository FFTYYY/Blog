(function() {

	var plugin_command = {
		exec: function(editor) {
			var text = editor.getData()

			var to_insert = "【乐谱开始】【吉他，4，4，4】【[1]|】【乐谱结束】"

			editor.insertHtml(to_insert);
		}
	}

	var plugin_name = "YMusic"
	CKEDITOR.plugins.add(plugin_name, {
		init: function(editor) {
			editor.addCommand(plugin_name, plugin_command)
			editor.ui.addButton("YMusic", {
				label: "PDF代码示例", 
				icon: this.path + "icon.gif",
				command: plugin_name
			});
		}
	})
})()

