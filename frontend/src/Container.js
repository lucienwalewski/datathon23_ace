import { makeStyles } from "@material-ui/core/styles";
import {
Card,
CardContent,
Typography,
List,
Grid,
Divider,
} from "@material-ui/core";

// Make a tile that displays the name and the impact below

const useStyles = makeStyles((theme) => ({
    root: {
        minWidth: 275,
        maxWidth: 275,
        minHeight: 275,
        maxHeight: 275,
        margin: 10,
        backgroundColor: "#f5f5f5",
        borderRadius: 10,
        boxShadow: "0px 0px 10px 0px rgba(0,0,0,0.2)",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
    },
    title: {
        fontSize: 14,
    },
    pos: {
        marginBottom: 12,
    },
    list: {
        width: "100%",
        maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
    },
}));

export default function Container({ data }) {
    const classes = useStyles();

    const tiles = [];

    for (let i = 0; i < data.length; i++) {
        const { name, impact, p_impact, n_impact, overall } = data[i];

        tiles.push(
            <Card className={classes.root} variant="outlined">
                <CardContent>
                    <Typography
                        className={classes.title}
                        color="textSecondary"
                        gutterBottom
                    >
                        {name}
                    </Typography>
                    <Typography variant="h5" component="h2">
                        {impact}
                    </Typography>
                </CardContent>
            </Card>
        );
    }

    return (
        <div className={classes.list}>
            <Grid container spacing={3}>
                {tiles}
            </Grid>
        </div>
    );
}