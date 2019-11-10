<template>
<div class="calculator">
  <div class="d-flex calculator__header" role="tab" id="wilksHeading">
    <a href="#wilksCollapse" class="nav-link h4" data-toggle="collapse"
       data-parent="#calcAccardion" aria-expanded="true" aria-controls="wilksCollapse">
      <font-awesome-icon icon="caret-down" size="lg" /> Wilks Coefficient
    </a>
  </div>
  <div id="wilksCollapse" class="calculator__body collapse" :class="{'show': show}"
       role="tabpanel" aria-labelledby="wilksHeading" data-parent="#calcAccardion">
    <form class="form-horizontal" role="form">
      <div class="form-body">
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Gender
          </label>
          <div class="col">
            <select class="form-control" @change="onChange($event.target.value)">
              <option value="Male" selected>Male</option>
              <option value="Female">Female</option>
            </select>
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Body weight
          </label>
          <div class="col">
            <input type="text" class="form-control" v-model="bodyWeight" placeholder="80"
                   @input="calculate">
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Lifted weight
          </label>
          <div class="col">
            <input type="text" class="form-control" v-model="liftedWeight" placeholder="120"
                   @input="calculate">
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Wilks
          </label>
          <div class="col">
            <input class="form-control" type="text" v-model="coefficient" readonly>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>
</template>

<script>
export default {
  name: 'Wilks',

  props: ['show'],

  data() {
    return {
      bodyWeight: 80,
      liftedWeight: 100,
      gender: 'Male',
      coefficient: 0,
    };
  },

  methods: {
    onChange(gender) {
      this.gender = gender;
      this.calculate();
    },

    calculate() {
      let a = -216.0475144;
      let b = 16.2606339;
      let c = -0.002388645;
      let d = -0.00113732;
      let e = 7.01863E-06;
      let f = -1.291E-08;
      if (this.gender === 'Female') {
        a = 594.31747775582;
        b = -27.23842536447;
        c = 0.82112226871;
        d = -0.00930733913;
        e = 0.00004731582;
        f = -0.00000009054;
      }
      const coefficient = 500 * this.liftedWeight / (a
          + b * this.bodyWeight
          + c * (this.bodyWeight ** 2)
          + d * (this.bodyWeight ** 3)
          + e * (this.bodyWeight ** 4)
          + f * (this.bodyWeight ** 5));
      this.coefficient = Math.round(coefficient * 100) / 100;
    },
  },

  mounted() {
    this.calculate();
  },
};
</script>

<style scoped>

</style>
