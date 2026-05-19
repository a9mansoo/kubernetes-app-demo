import { useState, useEffect } from 'react'
import API_URL from './api';
import Img from './assets/image.png'
import AvatarPic from "./assets/avatar.png"
import {
  Stack,
  Typography,
  Avatar,
  Card,
  CardHeader,
  CardMedia,
  CardContent,
  IconButton
} from "@mui/material"
import FavoriteBorderIcon from "@mui/icons-material/FavoriteBorder"
import ChatBubbleOutlineOutlinedIcon from '@mui/icons-material/ChatBubbleOutlineOutlined'
import SendIcon from "@mui/icons-material/Send"
import Skeleton from '@mui/material/Skeleton';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {

    const loadUser = async () => {
    try {
      let response = (await fetch(`${API_URL}/user/1`));
      let resp_json = await response.json();
      if (resp_json?.user) {
        setUser({user: resp_json.user, img: AvatarPic});
      }
    } catch(err) {
      console.log(err);
    }
  }

  loadUser();

  }, [])


  return (
     <Stack
      sx={{
        minHeight: "100vh",
        backgroundColor: "#fafafa",
        alignItems: "center",
        paddingTop: 4
      }}
    >
      <Card
        sx={{
          width: 500,
          borderRadius: 3
        }}
      >
        <CardHeader
          avatar={
            <Avatar src={user?.img ?? ""}>
            </Avatar>
          }
          title={user?.user || "loading..."}
          subheader={user? "k8s cluster" : "loading..."}
        />

        { user? <CardMedia
          component="img"
          image={Img}
          alt="test-img"
        /> : <Skeleton variant="rectangular" height={300}/>}
        
        <Stack
          direction="row"
          spacing={1}
          sx={{
            padding: 1
          }}
        >
          <IconButton>
            <FavoriteBorderIcon/>
          </IconButton>

          <IconButton>
            <ChatBubbleOutlineOutlinedIcon />
          </IconButton>

          <IconButton>
            <SendIcon />
          </IconButton>
        </Stack>

        <CardContent>
          <Typography variant="body2">
            <strong>{user?.user}</strong> {user? "Getting these k8s working" : "Oh no! k8s is not working"}
          </Typography>
        </CardContent>
      </Card>
    </Stack>
  )
}

export default App
