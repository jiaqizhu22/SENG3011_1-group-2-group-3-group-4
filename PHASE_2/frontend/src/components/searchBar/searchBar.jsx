import React from 'react';
import './searchBar.css';
import {useState} from 'react'
import { DateRangePickerComponent } from '@syncfusion/ej2-react-calendars';


const SearchBar = () => (
    <div className="searchBar">
      <div class="container">
        <div class="column">
          <DateRangePickerComponent placeholder="Enter date range: "></DateRangePickerComponent>
        </div>
        <div class="column">
          <form>
            <label> 
              <input placeholder="Location" type="text" name="location" style={{width: "370px"}}/>
            </label>
            <input type="submit" value="Submit" />
          </form>
        </div>
        <div class="column">

        <form>
            <label>
              <input placeholder="Key terms seperated by commas" type="text" name="keyterms" style={{width: "370px"}}/>
            </label>
            <input type="submit" value="Submit" />
          </form>

        </div>
      </div>
    </div>
  )
export default SearchBar;