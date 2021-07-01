"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._active_videos = []
        self._video_state = {'PLAY':1, 'PAUSED':2, 'STOP':3}

        self._playlist = {}
        
        #Fetch the list of videos
        self._list_of_videos = []
        video_list = self._video_library.get_all_videos()
        for each_video in video_list:
            self._list_of_videos.append([each_video._title,
                                  each_video._video_id,
                                  [tag.strip() for tag in each_video._tags] if each_video._tags else [],
                                  ''
                                  ])
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        ord_video_set = self._list_of_videos 
        '''
        video_list = self._video_library.get_all_videos()
        for each_video in video_list:
            ord_video_set.append([each_video._title,
                                  each_video._video_id,
                                  [tag.strip() for tag in each_video._tags] if each_video._tags else []
                                  ])
        '''
        ord_video_set.sort()
        print("Here's a list of all available videos:")
        for each_video in ord_video_set:
            display_format = each_video[0] + ' ('+ each_video[1] +')'
            if each_video[3]:
                print(''+display_format + ' [%s]' %' '.join(map(str, each_video[2]))+ " - FLAGGED " + each_video[3])
            else:
                print(''+display_format + ' [%s]' %' '.join(map(str, each_video[2])))
        #print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = []
        index = [i for i, video in enumerate(self._list_of_videos) if video_id == video[1]]
        if index:
            video = self._list_of_videos[index[0]]

        #video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
        else:
            if video[3]:
                print("Cannot play video: Video is currently flagged " + video[3])
            elif self._active_videos:
                #print("Stopping video: "+ self._video_library.get_video(self._active_videos.pop())._title)
                self.stop_video()
                self._active_videos.append([video_id, self._video_state.get('PLAY')])
                print("Playing video: "+ video[0])
            else:
                self._active_videos.append([video_id, self._video_state.get('PLAY')])
                print("Playing video: "+ video[0])
        #print(self._active_videos)
        #print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""

        if not self._active_videos:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: "+ self._video_library.get_video(self._active_videos.pop()[0])._title)
            

        '''print("stop_video needs implementation")'''

    def play_random_video(self):
        """Plays a random video from the video library."""

        if all(video[3] != '' for video in self._list_of_videos):
            print("No videos available")
        else:
            random_num = random.randint(0, len(self._list_of_videos)-1)
            self.play_video(self._list_of_videos[random_num][1])

        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if not self._active_videos:
            print("Cannot pause video: No video is currently playing")
        elif self._active_videos[0][1] == self._video_state.get('PAUSED'):
            print("Video already paused: " + self._video_library.get_video(self._active_videos[0][0])._title)
        else:
            self._active_videos[0][1] = self._video_state.get('PAUSED')
            print("Pausing video: " + self._video_library.get_video(self._active_videos[0][0])._title)

        #print(self._active_videos)
        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        if not self._active_videos:
            print("Cannot continue video: No video is currently playing")
        else:
            current_state = self._active_videos[0][1]
            if current_state == self._video_state.get('PAUSED'):
                self._active_videos[0][1] = self._video_state.get('PLAY')
                print("Continuing video: " + self._video_library.get_video(self._active_videos[0][0])._title)
            else:
                print("Cannot continue video: Video is not paused")
                
        
        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        
        if not self._active_videos:
            print("No video is currently playing")
        else:
            for each_video in self._list_of_videos:
                if self._active_videos[0][0] in each_video:
                    current_video = each_video
                    break
            
            if self._active_videos[0][1] == self._video_state.get('PAUSED'):
                print("Currently playing: "+ current_video[0] + ' ('+ current_video[1] +')' +' [%s]' %' '.join(map(str, current_video[2])) + ' - PAUSED')
            else:
                print("Currently playing: "+ current_video[0] + ' ('+ current_video[1] +')' +' [%s]' %' '.join(map(str, current_video[2])))
        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if any(playlist_name.upper() == p1 for p1 in self._playlist):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlist[playlist_name.upper()] = [playlist_name]
            print("Successfully created new playlist:", playlist_name)
        
        #print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video=[]
        index = [i for i, video in enumerate(self._list_of_videos) if video_id == video[1]]
        if index:
            video = self._list_of_videos[index[0]]
        
        if not any(playlist_name.upper() == p1 for p1 in self._playlist):
            print("Cannot add video to "+ playlist_name +": Playlist does not exist")
        elif any(video_id in self._playlist[p1] for p1 in self._playlist):
            print("Cannot add video to " + playlist_name + ": Video already added")
        elif not any(video_id == video[1] for video in self._list_of_videos):
            print("Cannot add video to " + playlist_name + ": Video does not exist")
        elif video[3]:
            print("Cannot add video to " + playlist_name + ": Video is currently flagged " + video[3])
        else:
            self._playlist[playlist_name.upper()].append(video_id)
            print("Added video to " + playlist_name + ": " + self._video_library.get_video(video_id)._title)                       

        #print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        if not self._playlist:
            print("No playlists exist yet")
        else:
            ord_playlist = [video for video in self._playlist]
            ord_playlist.sort()
            print("Showing all playlists:")
            for playlist in ord_playlist:
                print(" " + self._playlist[playlist][0])
        #print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        counter = 1
        if not playlist_name.upper() in self._playlist:
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")
        else:
            print("Showing playlist: " + playlist_name)
            if len(self._playlist[playlist_name.upper()]) == 1:
                print(" No videos here yet")
            else:
                while(counter < len(self._playlist[playlist_name.upper()])):
                    index = [i for i, video in enumerate(self._list_of_videos) if video[1] == self._playlist[playlist_name.upper()][counter]]
                    title = self._list_of_videos[index[0]][0]
                    vid_id = self._list_of_videos[index[0]][1]
                    tags = self._list_of_videos[index[0]][2]
                    flag_reason = self._list_of_videos[index[0]][3]
                    if flag_reason:
                        print(" " + title + " (" + vid_id + ")"+' [%s]' %' '.join(map(str, tags)) + " - FLAGGED " + flag_reason)
                    else:
                        print(" " + title + " (" + vid_id + ")"+' [%s]' %' '.join(map(str, tags)))

                    counter = counter + 1
        
        #print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        if not any(playlist_name.upper() == p1 for p1 in self._playlist):
            print("Cannot remove video from "+ playlist_name +": Playlist does not exist")
        elif not any(video_id == video[1] for video in self._list_of_videos):
            print("Cannot remove video from " + playlist_name + ": Video does not exist")            
        elif not any(video_id in self._playlist[p1] for p1 in self._playlist):
            print("Cannot remove video from " + playlist_name + ": Video is not in playlist")
        else:
            self._playlist[playlist_name.upper()].remove(video_id)
            print("Removed video from " + playlist_name + ": " + self._video_library.get_video(video_id)._title)                               

        #print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if not any(playlist_name.upper() == p1 for p1 in self._playlist):
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")
        else:
            self._playlist[playlist_name.upper()] = [self._playlist[playlist_name.upper()][0]]
            print("Successfully removed all videos from " + playlist_name)

        #print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if not any(playlist_name.upper() == p1 for p1 in self._playlist):
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")
        else:
            del self._playlist[playlist_name.upper()]
            print("Deleted playlist: " + playlist_name)

        #print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        ord_list = []
        counter = 1
        index = [i for i, video in enumerate(self._list_of_videos) if search_term.upper() in video[0].upper()]
        if not index:
            print("No search results for " + search_term)
            return

        for i in index:
            title = self._list_of_videos[i][0]
            ord_list.append((title,i))

        ord_list.sort()
        
        print("Here are the results for " + search_term +":")
        for i in ord_list:
            title = self._list_of_videos[i[1]][0]
            vid_id = self._list_of_videos[i[1]][1]
            tags = self._list_of_videos[i[1]][2]
            flag_reason = self._list_of_videos[i[1]][3]
            if not flag_reason:
                print(" " + str(counter) + ") " + title + " (" + vid_id + ")"+' [%s]' %' '.join(map(str, tags)))
                counter = counter + 1
            

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        user_resp = input()
        if user_resp.isnumeric():
            if int(user_resp) <= len(index):
                selected_video = self._list_of_videos[ord_list[int(user_resp)-1][1]][1]
                self.play_video(selected_video)
        #print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        ord_list = []
        counter = 1
        index = [i for i, video in enumerate(self._list_of_videos) if any(video_tag.upper() == tag.upper() for tag in video[2])]
        
        if not index:
            print("No search results for " + video_tag)
            return
        
        for i in index:
            title = self._list_of_videos[i][0]
            ord_list.append((title,i))

        ord_list.sort()
      
        print("Here are the results for " + video_tag +":")
        for i in ord_list:
            title = self._list_of_videos[i[1]][0]
            vid_id = self._list_of_videos[i[1]][1]
            tags = self._list_of_videos[i[1]][2]
            flag_reason = self._list_of_videos[i[1]][3]
            if not flag_reason:
                print(" " + str(counter) + ") " + title + " (" + vid_id + ")"+' [%s]' %' '.join(map(str, tags)))
                counter = counter + 1

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        user_resp = input()
        if user_resp.isnumeric():
            if int(user_resp) <= len(ord_list):
                selected_video = self._list_of_videos[ord_list[int(user_resp)-1][1]][1]
                self.play_video(selected_video)        
        #print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        need_to_flag = False
        if not any(video_id == video[1] for video in self._list_of_videos):
            print("Cannot flag video: Video does not exist")
        else:
            index = [i for i, video in enumerate(self._list_of_videos) if video_id == video[1]]
            video = self._list_of_videos[index[0]]
            if video[3]:
                print("Cannot flag video: Video is already flagged")
            else:
                need_to_flag = True

        if need_to_flag:
            if self._active_videos:
                if self._active_videos[0][1] in (self._video_state.get('PLAY'),self._video_state.get('PAUSED')) and self._active_videos[0][0] == video_id:
                   self.stop_video()
            
            if flag_reason:
                video[3] = "(reason: " + flag_reason + ")"
            else:
                video[3] = "(reason: Not supplied)"

            print("Successfully flagged video: " + video[0] + " " + video[3])
        #print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """

        need_to_unflag = False
        if not any(video_id == video[1] for video in self._list_of_videos):
            print("Cannot remove flag from video: Video does not exist")
        else:
            index = [i for i, video in enumerate(self._list_of_videos) if video_id == video[1]]
            video = self._list_of_videos[index[0]]
            if video[3] == '':
                print("Cannot remove flag from video: Video is not flagged")
            else:
                video[3] = ''
                print("Successfully removed flag from video: " + video[0])

        #print("allow_video needs implementation")
