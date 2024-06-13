import React, { Component } from 'react';

class ListaCursos extends Component {
    state = {
        data: [],
        loaded: false
    }

    componentDidMount() {
        fetch("http://localhost:8000/cursos/")
          .then(response => {
            if (response.status > 400) {
            }
            return response.json();
          })
          .then(data => {
            this.setState(() => {
              return {
                data,
                loaded: true
              };
            });
          });
      }
    
      render() {
        return (
            <div>
            {this.state.data.map(curso => {
              return (
                <h2 key={curso.id} className='App-table'>
                  {curso.descricao}
                </h2>
              );
            })}
          </div>
        );
      }
    }

export default ListaCursos;