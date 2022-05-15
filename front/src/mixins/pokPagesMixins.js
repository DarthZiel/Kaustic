import axios from 'axios'
import {mapGetters} from 'vuex'
import {mapMutations} from 'vuex'
export default{
    data(){
        return{
            imageUrl: [],
            pokemons: [],
            globalPokemons: []
        }
    },
    created() {
        this.$store.dispatch('axiosPokemons')
    },
    mounted() {
        this.checkPokemonsStore()
        console.log(this.$store.getters.allPokemons[1]);
        // console.log(this.allPokemons);

    },
    beforeUpdate() {
        this.createPokemonsNow()          
    },
    methods: {
        axiosGetPokemons() {
            axios
            .get(`https://pokeapi.co/api/v2/pokemon/${this.id}`)
            .then(response => (
                this.pokemons = response.data, 
                this.imageUrl = response.data.sprites.other.dream_world.front_default
                ))
        },
        checkPokemonsStore() {
            for (let i = 0; i < this.loadingPokemons.length; i++) {
                if (this.loadingPokemons[i].id === this.id) {
                    this.pokemons = this.loadingPokemons[i].pokemons
                }else{
                    this.axiosGetPokemons()
                    break;
                }
                
            }
        },
        createPokemonsNow() {
            for (let i = 0; i < this.loadingPokemons.length; i++) {
                if (this.id === this.loadingPokemons[i].id) {
                    break;
                }else{
                    this.createPokemons({
                        id: this.pokemons.id,
                        pokemons: this.pokemons
                    })
                    break;
                }
            }
        },
        randomId() {
            this.id = Math.floor(Math.random() * 649) + 1
        },
        ...mapMutations(['createPokemons'])
    },
    computed: {
        ...mapGetters(['allPokemons']),
        ...mapGetters(['loadingPokemons'])
    }
}