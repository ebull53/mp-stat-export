import web
import csv
import time

urls = ('/home','home','/upload', 'Upload','/mp','mp')


class home:
    def GET(self):
        return """<html><head></head><body>
        <form method="POST" enctype="multipart/form-data" action="">
        Be sure to add all jersey numbers to your exported file.
        <br/>
        Also add games played in the match to the 3rd column titled MP.
        <br/>
        After Uploading you wil lsee a print out of your stats in the MaxPreps import format, Right click and save as a text file for import to Max Preps
<br/>
<br/>
<input type="submit" value="Continue to upload page"/>
</form>
</body></html>"""
    def POST(self):
        raise web.seeother('/upload')


class Upload:
    def GET(self):
        return """<html><head>Select your exported file</head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""
    def POST(self):
        x = web.input(myfile={})
        filedir = 'Website/static' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created # splits the and chooses the last part (the filename with extension)
            fout = open('static/data.csv','w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        raise web.seeother('/mp')

class mp:
    def GET(self):
        number=[]
        match_GamesPlayed=[]
        S_Att=[]
        Ace=[]
        S_Err=[]
        S_Pts_W=[]
        H_Att=[]
        Kill=[]
        H_Err=[]
        SR_Success=[]
        SR_Err=[]
        B_Solo=[]
        B_Assist=[]
        BlockErrors=[]
        BallHandling_Attempt=[]
        Assist=[]
        A_Err=[]
        Digs=[]
        DigErrors=[]
        master =[number,match_GamesPlayed,S_Att,Ace,S_Err,S_Pts_W,H_Att,Kill,H_Err,SR_Success,SR_Err,B_Solo,B_Assist,BlockErrors,BallHandling_Attempt,Assist,A_Err,Digs,DigErrors]

        first = True
        second = True
        count=-1

        with open('static/data.csv','rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if first:
                    first = False
                    continue
                if second:
                    second = False
                    continue
                number.append(row[0])
                match_GamesPlayed.append(row[2])
                S_Att.append(row[22])
                Ace.append(row[20])
                S_Err.append(row[21])
                S_Pts_W.append(row[16])
                H_Att.append(row[31])
                Kill.append(row[29])
                H_Err.append(row[30])
                SR_Success.append(row[25])
                SR_Err.append(row[26])
                B_Solo.append(row[34])
                B_Assist.append(row[35])
                BlockErrors.append(row[36])
                BallHandling_Attempt.append("0")
                Assist.append(row[37])
                A_Err.append(row[38])
                Digs.append(row[41])
                DigErrors.append("0")
                count += 1
        sline=""
        p="|"
        mp = open('static/maxpreps_file.txt', 'w')
        mp.write('Jersey|MatchGamesPlayed|TotalServes|ServingAces|ServingErrors|ServingPoints|AttacksAttempts|AttacksKills|AttacksErrors|ServingReceivedSuccess|ServingReceivedErrors|BlocksSolo|BlocksAssists|BlocksErrors|BallHandlingAttempt|Assists|AssistsErrors|Digs|DigsErrors\n')
        for player in number:
            playerline =[item[count] for item in master]
            sline = playerline[0]+p+playerline[1]+p+playerline[2]+p+playerline[3]+p+playerline[4]+p+playerline[5]+p+playerline[6]+p+playerline[7]+p+playerline[8]+p+playerline[9]+p+playerline[10]+p+playerline[11]+p+playerline[12]+p+playerline[13]+p+playerline[14]+p+playerline[15]+p+playerline[16]+p+playerline[17]+p+playerline[18]+"\n"
            count -=1
            mp.write(sline)
        raise web.seeother('/static/maxpreps_file.txt')


if __name__ == "__main__":
   app = web.application(urls, globals())
   app.run()
