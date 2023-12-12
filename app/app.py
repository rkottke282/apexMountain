from shiny import App, reactive, render, ui
from service.tmdb import getData

app_ui = ui.page_fluid(
    ui.panel_title("Apex Mountain"),
    ui.input_text("actorInput", "Enter Actor name"),
    ui.input_action_button("actorInputButton", "Search",class_="btn-primary"),
    ui.output_text_verbatim("actorSearchValue")
)


def server(input, output, session):
    
    @output
    @render.text
    async def actorSearchValue():
        input.actorInputButton()
        with reactive.isolate():
            input = input.actorInput()
            # if (input != None):
            #     data = getData(input)
            #     print(data)
            return f"{input.actorInput()}"
    


app = App(app_ui, server)
