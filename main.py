import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Cyber Dark Theme
Window.clearcolor = (0.04, 0.06, 0.1, 1)

class IgrisApp(App):
    def build(self):
        self.title = "IGRIS AI"
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        # Header
        layout.add_widget(Label(
            text="[b]⚡ IGRIS SYSTEM[/b]", 
            markup=True, 
            font_size="28sp", 
            color=(0, 0.85, 1, 1), 
            size_hint=(1, 0.15)
        ))
        
        # Response Box
        self.output_box = Label(
            text="IGRIS Online.\nAwaiting command...", 
            font_size="16sp", 
            color=(0.9, 0.9, 0.9, 1),
            text_size=(Window.width - 60, None),
            halign="center",
            valign="middle",
            size_hint=(1, 0.5)
        )
        layout.add_widget(self.output_box)
        
        # Input Box
        self.input_field = TextInput(
            hint_text="Ask IGRIS anything...", 
            multiline=False, 
            font_size="16sp", 
            size_hint=(1, 0.15),
            background_color=(0.12, 0.18, 0.28, 1),
            foreground_color=(1, 1, 1, 1)
        )
        layout.add_widget(self.input_field)
        
        # Send Button
        btn = Button(
            text="SEND COMMAND", 
            font_size="18sp", 
            bold=True, 
            background_color=(0, 0.75, 1, 1), 
            size_hint=(1, 0.2)
        )
        btn.bind(on_press=self.send_command)
        layout.add_widget(btn)
        
        return layout

    def send_command(self, instance):
        query = self.input_field.text.strip()
        if not query:
            return
        self.output_box.text = f"IGRIS Thinking: '{query}'..."
        self.input_field.text = ""
        
        # Agar Gemini API key hai to yahan daal sakte hain, warna baad me bhi daal sakte hain
        API_KEY = "YOUR_GEMINI_API_KEY_HERE"
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
        payload = {
            "contents": [{
                "parts": [{"text": f"You are IGRIS, an advanced AI assistant. Answer concisely: {query}"}]
            }]
        }
        
        try:
            res = requests.post(url, json=payload, timeout=12)
            if res.status_code == 200:
                reply = res.json()["candidates"][0]["content"]["parts"][0]["text"]
                self.output_box.text = f"[IGRIS]:\n\n{reply.strip()}"
            else:
                self.output_box.text = "API Error. Check API Key."
        except Exception as e:
            self.output_box.text = f"Connection Failed: {str(e)}"

if __name__ == "__main__":
    IgrisApp().run()
