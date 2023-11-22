import os
import pygame
from tkinter import Tk, Label, Listbox, Button, StringVar, messagebox, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Music Player")
        self.master.geometry("400x300")

        self.current_song_label = Label(master, text="Current Song: None")
        self.current_song_label.pack(pady=10)

        self.playlist_label = Label(master, text="Playlist:")
        self.playlist_label.pack()

        self.playlist_var = StringVar()
        self.playlist_box = Listbox(master, listvariable=self.playlist_var, selectmode="SINGLE", height=10)
        self.playlist_box.pack(pady=10)

        self.load_button = Button(master, text="Load Playlist", command=self.load_playlist)
        self.load_button.pack()

        self.play_button = Button(master, text="Play", command=self.play_song)
        self.play_button.pack(side="left", padx=10)

        self.pause_button = Button(master, text="Pause", command=self.pause_song)
        self.pause_button.pack(side="left", padx=10)

        self.stop_button = Button(master, text="Stop", command=self.stop_song)
        self.stop_button.pack(side="left", padx=10)

        self.add_button = Button(master, text="Add Song", command=self.add_song)
        self.add_button.pack(side="left", padx=10)

        self.song_list = []

    def load_playlist(self):
        playlist_path = filedialog.askopenfilename(filetypes=[("Playlist files", "*.txt")])
        if playlist_path:
            with open(playlist_path, "r") as file:
                self.song_list = file.read().splitlines()
            self.update_playlist()

    def update_playlist(self):
        self.playlist_box.delete(0, "end")
        for song in self.song_list:
            self.playlist_box.insert("end", os.path.basename(song))

    def play_song(self):
        selected_index = self.playlist_box.curselection()
        if selected_index:
            selected_song = self.song_list[selected_index[0]]
            pygame.mixer.init()
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()
            self.current_song_label.config(text=f"Current Song: {os.path.basename(selected_song)}")

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()
        self.current_song_label.config(text="Current Song: None")

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if song_path:
            self.song_list.append(song_path)
            self.update_playlist()

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()