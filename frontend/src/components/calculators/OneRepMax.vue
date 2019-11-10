<template>
<div class="calculator">
  <div class="d-flex caulculator__header" role="tab" id="ormHeading">
    <a href="#ormCollapse" class="nav-link h4" data-toggle="collapse"
       data-parent="#calcAccardion" aria-expanded="true" aria-controls="ormCollapse">
      <font-awesome-icon icon="caret-down" size="lg" /> One Repetition Maximum
    </a>
  </div>
  <div id="ormCollapse" class="calculator__body collapse" :class="{'show': showCalc }"
       role="tabpanel" aria-labelledby="ormHeading" data-parent="#calcAccardion">
    <form class="form-horizontal" role="form">
      <div class="form-body">
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Repetitions
          </label>
          <div class="col">
            <input type="text" class="form-control" v-model="reps" placeholder="5"
                   @input="calculate">
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Lifted weight
          </label>
          <div class="col">
            <input type="text" class="form-control" v-model="liftedWeight" placeholder="100"
                   @input="calculate">
          </div>
        </div>
        <div v-for="result in results" :key="result.formula" class="form-group row">
          <label class="col d-flex align-items-center">
            {{ result.formula }}
          </label>
          <div class="col">
            <input class="form-control" type="text" v-model="result.value" readonly>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>
</template>

<script>
export default {
  name: 'OneRepMax',

  props: ['show'],

  data() {
    return {
      showCalc: this.show,
      reps: 5,
      liftedWeight: 100,
      results: [
        { formula: 'Epley formula', value: 0 },
        { formula: 'Brzycki formula', value: 0 },
        { formula: 'Mcglothin formula', value: 0 },
        { formula: 'Lombardi formula', value: 0 },
        { formula: 'Mayhew formula', value: 0 },
        { formula: "O'Conner formula", value: 0 },
        { formula: 'Wathan formula', value: 0 },
        { formula: 'Average result', value: 0 },
      ],
    };
  },

  methods: {
    round(number, decimalPlaces) {
      return Math.round(number * (10 ** decimalPlaces)) / (10 ** decimalPlaces);
    },

    calculate() {
      this.results[0].value = this.round(this.calcEpley(), 2);
      this.results[1].value = this.round(this.calcBrzycki(), 2);
      this.results[2].value = this.round(this.calcMcGlothin(), 2);
      this.results[3].value = this.round(this.calcLombardi(), 2);
      this.results[4].value = this.round(this.calcMayhew(), 2);
      this.results[5].value = this.round(this.calcOConner(), 2);
      this.results[6].value = this.round(this.calcWathan(), 2);
      this.results[7].value = this.round(this.calcAvg(), 2);
    },

    calcEpley() {
      return this.liftedWeight * (1 + this.reps / 30);
    },

    calcBrzycki() {
      return this.liftedWeight * 36 / (37 - this.reps);
    },

    calcMcGlothin() {
      return 100 * this.liftedWeight / (101.3 - 2.67123 * this.reps);
    },

    calcLombardi() {
      return this.liftedWeight * (this.reps ** 0.1);
    },

    calcMayhew() {
      return 100 * this.liftedWeight / (52.2 + 41.9 * (Math.E ** (-0.055 * this.reps)));
    },

    calcOConner() {
      return this.liftedWeight * (1 + this.reps / 40);
    },

    calcWathan() {
      return 100 * this.liftedWeight / (48.8 + 53.8 * (Math.E ** (-0.075 * this.reps)));
    },

    calcAvg() {
      let sum = 0;
      const FORMULAS_COUNT = 7;
      for (let i = 0; i < FORMULAS_COUNT; i += 1) {
        sum += this.results[i].value;
      }
      return sum / FORMULAS_COUNT;
    },
  },

  mounted() {
    this.calculate();
  },
};
</script>

<style scoped>

</style>
