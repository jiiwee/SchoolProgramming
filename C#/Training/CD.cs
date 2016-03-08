using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OlioLuokka
{
    class CD
    {
        public string Artist { get; set; }
        public string Album { get; set; }
        public string Genre { get; set; }
        public double Price { get; set; }
        public List<Song> Songs;

        public CD(string artist, string album, string genre, double price)
        {
            Artist = artist;
            Album = Album;
            Genre = genre;
            Price = price;
            Songs = new List<Song>();
        }

        public void AddSong(Song song)
        {
            Songs.Add(song);
        }

        public override string ToString()
        {
            string data = "CD";
            data += "\nArtist : " + Artist + "\nAlbum : " + Album + "\nGenre : " + Genre + "\nGenre : " + "Price : " + Price + "e";
            data += "\nSongs:";

            int totalLength = 0;
            foreach(Song song in Songs)
            {
                if (song != null)
                {
                    data += "\n" + ". " + song.ToString();
                    totalLength = song.LengthInSeconds;
                }
            }

            int min = totalLength / 60;
            int sec = totalLength % 60;
            string duration = min.ToString("00") + ":" + sec.ToString("00");
            data += "\nTotal duration : " + duration;
            return data;
        }
    }
}
