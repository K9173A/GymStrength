<template>
<div class="calculator">
  <div class="d-flex calculator__header" role="tab" id="bmrHeading">
    <a href="#bmrCollapse" class="nav-link h4" data-toggle="collapse"
       data-parent="#calcAccardion" aria-expanded="true" aria-controls="bmrCollapse">
      <font-awesome-icon icon="caret-down" size="lg" /> Basal Metabolic Rate
    </a>
  </div>
  <div id="bmrCollapse" class="calculator__body collapse" :class="{'show': show}"
       role="tabpanel" aria-labelledby="bmrHeading" data-parent="#calcAccardion">
    <form class="form-horizontal" role="form">
      <div class="form-body">
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Units
          </label>
          <div class="col">
            <select class="form-control" @change="onChangeUnits($event.target.value)">
              <option value="Metric" selected>Metric</option>
              <option value="Imperial">Imperial</option>
            </select>
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Gender
          </label>
          <div class="col">
            <select class="form-control" @change="onChangeGender($event.target.value)">
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
            <div class="input-group">
              <input type="text" class="form-control" v-model="bodyWeight"
                     placeholder="80" @input="calculate">
              <div class="input-group-append">
                <span class="input-group-text" id="idWeight">
                  kg
                </span>
              </div>
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Age
          </label>
          <div class="col">
            <input type="text" class="form-control" v-model="age" placeholder="25"
                   @input="calculate">
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Height
          </label>
          <div class="col">
            <div class="input-group">
              <input type="text" class="form-control" v-model="height"
                     placeholder="180" @input="calculate">
              <div class="input-group-append">
                <span class="input-group-text" id="idHeight">
                  cm
                </span>
              </div>
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Activity
          </label>
          <div class="col">
            <select class="form-control" @change="onChangeActivity($event.target.value)">
              <option value="1.2" selected>
                No physical activity
              </option>
              <option value="1.375">
                Light activity (1-3 workouts per week)
              </option>
              <option value="1.55">
                Moderate activity (3-5 workouts per week)
              </option>
              <option value="1.725">
                Intense activity (5-7 intense workouts per week)
              </option>
              <option value="1.9">
                Very intense activity (sports & physical job)
              </option>
            </select>
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Harris-Benedict formula
          </label>
          <div class="col">
            <input class="form-control" type="text" v-model="bmrHarrisBenedict" readonly>
          </div>
        </div>
        <div class="form-group row">
          <label class="col d-flex align-items-center">
            Mifflin-St.Jeor formula
          </label>
          <div class="col">
            <input class="form-control" type="text" v-model="bmrMifflinStJeor" readonly>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>
</template>

<script>
export default {
  name: 'BMR',

  props: ['show'],

  data() {
    return {
      showCalc: this.show,
      units: 'Metric',
      gender: 'Male',
      bodyWeight: 80,
      age: 25,
      height: 180,
      activity: 1.2,
      bmrHarrisBenedict: 0,
      bmrMifflinStJeor: 0,
    };
  },

  methods: {
    onChangeUnits(units) {
      document.getElementById('idHeight').innerText = units === 'Metric' ? 'cm' : 'ft';
      document.getElementById('idWeight').innerText = units === 'Metric' ? 'kg' : 'lbs';
      this.units = units;
      this.calculate();
    },

    onChangeGender(gender) {
      this.gender = gender;
      this.calculate();
    },

    onChangeActivity(activity) {
      this.activity = activity;
      this.calculate();
    },

    calculate() {
      this.bmrHarrisBenedict = this.calcHarrisBenedict().toFixed();
      this.bmrMifflinStJeor = this.calcMifflinStJeor().toFixed();
    },

    calcHarrisBenedict() {
      let bmr = 0;
      if (this.gender === 'Male' && this.units === 'Metric') {
        bmr = 66.5 + 13.75 * this.bodyWeight + 5.003 * this.height - 6.755 * this.age;
      } else if (this.gender === 'Male' && this.units === 'Imperial') {
        bmr = 66 + 6.2 * this.bodyWeight + 12.7 * this.height - 6.76 * this.age;
      } else if (this.gender === 'Female' && this.units === 'Metric') {
        bmr = 655.1 + 9.563 * this.bodyWeight + 1.85 * this.height - 4.676 * this.age;
      } else if (this.gender === 'Female' && this.units === 'Imperial') {
        bmr = 655.1 + 4.35 * this.bodyWeight + 4.7 * this.height - 4.7 * this.age;
      }
      bmr *= this.activity;
      return bmr;
    },

    calcMifflinStJeor() {
      let bmr = 0;
      if (this.gender === 'Male' && this.units === 'Metric') {
        bmr = 10 * this.bodyWeight + 6.25 * this.height - 5 * this.age + 5;
      } else if (this.gender === 'Male' && this.units === 'Imperial') {
        bmr = 10 / 2.205 * this.bodyWeight + 6.25 / 30.48 * this.height - 5 * this.age + 5;
      } else if (this.gender === 'Female' && this.units === 'Metric') {
        bmr = 10 * this.bodyWeight + 6.25 * this.height - 5 * this.age - 161;
      } else if (this.gender === 'Female' && this.units === 'Imperial') {
        bmr = 10 / 2.205 * this.bodyWeight + 6.25 * 30.48 * this.height - 5 * this.age - 161;
      }
      bmr *= this.activity;
      return bmr;
    },
  },

  mounted() {
    this.calculate();
  },
};
</script>

<style scoped>

</style>
