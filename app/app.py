from shiny import App, reactive, render, ui
from service.tmdb import getData
from matplotlib import pyplot as plt
import pandas as pd

app_ui = ui.page_fluid(
    ui.panel_title("Apex Mountain"),
    ui.input_text("actorInput", "Enter Actor name"),
    ui.input_action_button("actorInputButton", "Search",class_="btn-primary"),
    ui.output_text_verbatim("actorSearchValue"),
    ui.output_plot("actorMoviePlot")
)

def server(input, output, session):
    
    @output
    @render.text
    async def actorSearchValue():
        input.actorInputButton()
        with reactive.isolate():
            return input.actorInput()

    @output
    @render.plot
    async def actorMoviePlot():
        input.actorInputButton()
        with reactive.isolate():
            if (input.actorInput() == ""):
                return None
            else:
                movie_data = getData(input.actorInput())
                plt.xticks(rotation=45)
                for (i, j,k) in zip (movie_data['release_date'], movie_data['popularity'], movie_data['title']):
                    plt.text(i, j, f'{k}', ha='center')
                return plt.plot(movie_data['release_date'], movie_data['popularity'])
            
app = App(app_ui, server)
